import plotly.graph_objects as go
import random
import Registry

def see_map(sensor_locations, temperatures):
    fig = go.Figure()

    bubble_size = 30  # Larger bubble size

    x = 10
    y = 15
    counter = 0

    for sensor, location in sensor_locations:
        x_position = x
        y_position = y
        counter += 1

        if counter == 5:
            x += 10
            y = 15  # Reset y for the next column
            counter = 0
        else:
            y += 15  # Increment y for the next bubble in the column

        text = f"{sensor.ID}<br>{location.name}<br>{temperatures.findTemperature(sensor.ID):.2f}°C"

        fig.add_trace(go.Scatter(
            x=[x_position],
            y=[y_position],
            mode='markers+text',
            marker=dict(size=bubble_size, color='blue'),
            text=text,
            name=f"{sensor.ID} - {location.name}",
            textposition="middle right",
        ))

    # Create data for grey bubbles with the same pattern
    for no_sensor_location in Registry.AVAILABLE_CITIES:
        x_position = x
        y_position = y
        counter += 1

        if counter == 5:
            x += 10
            y = 15  # Reset y for the next column
            counter = 0
        else:
            y += 15  # Increment y for the next bubble in the column

        text = f"{no_sensor_location}"

        fig.add_trace(go.Scatter(
            x=[x_position],
            y=[y_position],
            mode='markers+text',
            marker=dict(size=bubble_size, color='grey'),
            text=text,
            name=f"{no_sensor_location}",
            textposition="middle right",
        ))

    # Calculate the width and height based on the number of columns and rows
    num_columns = len(sensor_locations) // 5
    width = max(1450, 50 * num_columns)  # Adjusted width to 1250
    height = 800  # Adjusted height to 800

    fig.update_layout(
        title='Sensor Temperature System',
        xaxis_title='',
        yaxis_title='',
        xaxis_showticklabels=False,
        yaxis_showticklabels=False,
        xaxis_showgrid=False,  # Remove x-axis grid
        yaxis_showgrid=False,  # Remove y-axis grid
        width=width,
        height=height,
    )

    fig.show()
