import matplotlib.pyplot as plt
import Registry


def visualize_sensor_data(sensor_locations, temperatures):
    fig, ax = plt.subplots()

    circle_spacing = 0.4

    # Count the number of locations with sensors
    num_locations_with_sensors = len(sensor_locations)

    # create blue bubbles for all locations with a sensor
    for index,(sensor, location) in enumerate(sensor_locations):
        color = 'blue'
        text = f" {location.name}\n {sensor.ID}\nTemp: {temperatures.findTemperature(sensor.ID)}°C"

        x_position = index*circle_spacing-0.2
        bubble = plt.Circle((x_position, 0), 0.2, color=color, alpha=0.7)
        ax.add_patch(bubble)
        ax.annotate(text, (x_position, 0), ha='center', va='center', color='white', fontsize=8)

    # create grey bubbles for locations without sensors
    for no_sensor_location in Registry.AVAILABLE_CITIES:
        if all(no_sensor_location != sensor_loc[1].name for sensor_loc in sensor_locations):
            x_position = num_locations_with_sensors * circle_spacing - 0.2
            bubble = plt.Circle((x_position, 0), 0.2, color='grey', alpha=0.7)
            ax.add_patch(bubble)
            ax.annotate(no_sensor_location, (x_position, 0), ha='center', va='center', color='white', fontsize=8)
            num_locations_with_sensors += 1

    ax.set_xlim(-circle_spacing, (num_locations_with_sensors-1) * circle_spacing)
    ax.set_ylim(-1, 1)
    plt.title('Sensor Temperature System')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()
