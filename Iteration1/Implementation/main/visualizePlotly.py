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

        temp = temperatures.findTemperature(sensor.ID)
        text = f"{sensor.ID}<br>{location.name}<br>{temp:.2f}°C"

        blueVal = 255-3.1875*(temp+40)
        redVal =3.1875*(temp+40)
        color = [redVal, 0, blueVal]
        fig.add_trace(go.Scatter(

            #marker=dict(size=bubble_size, color=[[255-3.1875*(temp+40),3.1875*(temp+40),0]])),
            x=[x_position],
            y=[y_position],
            mode='markers+text',
            marker=dict(size=bubble_size, color='rgb('+str(color[0])+','+str(color[1])+','+str(color[2])+')'),
            text=text,
            name=f"{sensor.ID} - {location.name}",
            textposition="middle right",
        ))

    # Create data for grey bubbles with the same pattern
    #for no_sensor_location in set(Registry.AVAILABLE_CITIES)-set([location.name for sensor, location in sensor_locations]):
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

    # Add text containing errors below the map
    fig.add_annotation(
        x=0.5,
        y=-0.1,
        xref='paper',
        yref='paper',
        text='ERROR: Cannot connect to sensor network',
        showarrow=False,
        font=dict(
            family='Arial',
            size=16,
            color='red'
        )
    )
    
    fig.show()
