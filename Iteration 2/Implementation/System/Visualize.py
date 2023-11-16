import plotly.graph_objects as go
import random
import Registries.LocationRegistry as LocationRegistry

def see_map(system):
    fig = go.Figure()
    bubble_size = 30  # Larger bubble size
    x = 10
    y = 15
    counter = 0
    for location in LocationRegistry.AVAILABLE_CITIES:
        x_position = x
        y_position = y
        counter += 1
        sensor = system.map.fromLocation(location)
        if counter == 5:
            x += 10
            y = 15  # Reset y for the next column
            counter = 0
        else:
            y += 15  # Increment y for the next bubble in the column
        if sensor == None:
            text = f"{location}"
            color = color='grey'
            name = str(f"{location}")
        else:
            temp = system.readTemperature(location)
            sensStr = f'sensor#{sensor.sensorID}'
            text = f"{sensStr}<br>{location}<br>{temp:.2f}°C"
            blueVal = 255-3.1875*(temp+40)
            redVal =3.1875*(temp+40)
            color = 'rgb('+str(redVal)+',0,'+str(blueVal)+')'
            name = str(f"{sensor.sensorID} - {location}")
        fig.add_trace(go.Scatter(
            #marker=dict(size=bubble_size, color=[[255-3.1875*(temp+40),3.1875*(temp+40),0]])),
            x=[x_position],
            y=[y_position],
            mode='markers+text',
            marker=dict(size=bubble_size, color=color),
            text=text,
            name=name,
            textposition="middle right",
        ))

    # Calculate the width and height based on the number of columns and rows
   
    num_columns = len(LocationRegistry.AVAILABLE_CITIES) // 5
    width = max(1250, 50 * num_columns)  # Adjusted width to 1250
    height = 800
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
    
def see_location_temperatures(loctemps):
    fig = go.Figure()
    bubble_size = 30  # Larger bubble size
    x = -15
    y = 5
    counter = 0
    for loctemp in loctemps:
        x_position = x
        y_position = y
        counter += 1
        y += 15  # Reset y for the next column
        temp = loctemp.temperature.value
        text = f"{loctemp.location.name} : {temp:.2f}°C"
        blueVal = 255-3.1875*(temp+40)
        redVal =3.1875*(temp+40)
        color = 'rgb('+str(redVal)+',0,'+str(blueVal)+')'
        name = str(f"{loctemp.location.name}")
        fig.add_trace(go.Scatter(
            #marker=dict(size=bubble_size, color=[[255-3.1875*(temp+40),3.1875*(temp+40),0]])),
            x=[x_position],
            y=[y_position],
            mode='markers+text',
            marker=dict(size=bubble_size, color=color),
            text=text,
            name=name,
            textposition="middle right",
        ))
    
    num_rows = len(loctemps)
    height = max(550, 50 * num_rows)  # Adjusted width to 1250
    width = 500
    fig.update_layout(
        title='     Location Temperatures',
        xaxis_title='',
        yaxis_title='',
        xaxis_showticklabels=False,
        yaxis_showticklabels=False,
        xaxis_showgrid=False,  # Remove x-axis grid
        yaxis_showgrid=False,  # Remove y-axis grid
        width=width,
        height=height,
        margin=dict(l=0, r=0, t=50, b=50)
    )
    fig.show()

