<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sweating Feet Control</title>
    <style>
        body {
            background: linear-gradient(90deg, rgb(0, 143, 225), aqua, lightblue);
            margin: 0;
            padding: 0;
        }
        nav {
            background-color: black;
            overflow: hidden;
            box-shadow: 0 6px 12px white;
        }
        nav ul {
            list-style-type: none;
            display: flex;
            margin: 0;
            padding: 20px;
            text-align: center;
            justify-content: center;
        }
        nav ul li {
            padding: 0;
            font-size: 20px;
        }
        nav ul li a {
            padding: 10px;
            font-size: 25px;
            text-decoration: none;
            color: white;
            align-items: center;
            text-align: center;
        }
        pre {
            color: white;
            background-color: black;
            font-style: bold;
            text-align: center;
        }
        main {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 20px;
            margin: 20px;
            align-items: center;
            text-align: center;
        }
        .card {
            background-color: aliceblue;
            width: 270px;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 4px 8px pink;
            box-sizing: 100px;
            height: 210px;
        }
        button {
            background-color: rgb(232, 146, 146);
            color: white;
            padding: 30px;
            border-radius: 100px;
            display: flex;
            box-sizing: initial;
            align-items: center;
            text-align: center;
            width: 230px;
        }
        button:hover {
            background-color: rgb(227, 158, 209);
            color: black;
        }
        .card2 {
            color: black;
            font-style: normal;
            background-color: white;
            padding: 10px;
            border-radius: 10px;
            align-items: center;
            text-align: center;
            margin: 50px;
            height: 250px;
        }
        .dashboard {
            color: black;
            background-color: rgb(240, 240, 163);
            padding: 10px;
            border-radius: 5px;
            align-items: center;
            text-align: center;
            margin: 4px;
            width: 200px;
            height: 25px;
        }
        .dashboard1 {
            color: black;
            background-color: rgb(213, 163, 240);
            padding: 10px;
            border-radius: 5px;
            align-items: center;
            text-align: center;
            margin: 4px;
            width: 200px;
            height: 25px;
        }
        .dashboard2 {
            color: black;
            background-color: rgb(163, 231, 240);
            padding: 10px;
            border-radius: 5px;
            align-items: center;
            text-align: center;
            margin: 4px;
            width: 200px;
            height: 25px;
        }
        .dashboard3 {
            color: black;
            background-color: rgb(240, 172, 163);
            padding: 10px;
            border-radius: 5px;
            align-items: center;
            text-align: center;
            margin: 4px;
            width: 200px;
            height: 25px;
        }
        .chart-container {
            background-color: aliceblue;
            width: 570px;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 4px 8px pink;
            box-sizing: 100px;
            height: 350px;
        }
        canvas {
            width: 100%;
            height: 100%;
        }
    </style>
</head>
<body>
    <nav>
        <h1><ul><li><a href="#">Sweating Feet Control</a></li></ul></h1>
        <h3><pre>Monitor and Control Your Sweaty Feet</pre></h3>
    </nav>

    <main>
        <div class="card" id="liveData">
            <h3>Live Data</h3>
            <p><b>Temperature:</b> <span id="temp">Loading...</span> °C</p>
            <p><b>Humidity:</b> <span id="Hum">Loading...</span></p>
            <p><b>Heat Level:</b> <span id="heat">Loading...</span></p>
            <p><b>Cool Level:</b> <span id="cool">Loading...</span></p>
        </div>

        <div class="card2" id="SensoryAlerts">
            <h3>Alerts</h3>
            <div class="dashboard" id="tempAlert">Loading...</div>
            <div class="dashboard1" id="humAlert">Loading...</div>
            <div class="dashboard2" id="heatAlert">Loading...</div>
            <div class="dashboard3" id="coolAlert">Loading...</div>
        </div>

        <div class="chart-container">
            <h1>Live Graph</h1>
            <canvas id="tempChart"></canvas>
        </div>
    </main>

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        // Fetch data from the API
        async function fetchData() {
            try {
                const tempResponse = await fetch('/api/temperature');
                const humResponse = await fetch('/api/humidity');
                const heatResponse = await fetch('/api/heatLevel');
                const coolResponse = await fetch('/api/coolLevel');

                const temp = await tempResponse.json();
                const hum = await humResponse.json();
                const heat = await heatResponse.json();
                const cool = await coolResponse.json();

                // Update Live Data
                document.getElementById('temp').textContent = temp.value;
                document.getElementById('Hum').textContent = hum.value + '%';
                document.getElementById('heat').textContent = heat.value + ' joules';
                document.getElementById('cool').textContent = cool.value + ' W';

                // Update Alerts
                document.getElementById('tempAlert').textContent = temp.value > 30 ? "High Temperature Detected!" : "Temperature is Normal";
                document.getElementById('humAlert').textContent = hum.value < 50 ? "Low Humidity Detected" : "Humidity Levels are Stable";
                document.getElementById('heatAlert').textContent = heat.value > 300 ? "High Heat Detected!" : "Heat Level is Stable";
                document.getElementById('coolAlert').textContent = cool.value < 100 ? "Cool Level Unstable!" : "Cool Level is Stable";
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        }

        // Fetch initial data when the page loads
        fetchData();
        setInterval(fetchData, 5000); // Refresh every 5 seconds

        // Chart.js graph for temperature data
        const ctx = document.getElementById('tempChart').getContext('2d');
        const tempData = [22, 23, 24, 27, 30];
        const tempChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['1s', '2s', '3s', '4s', '5s'],
                datasets: [{
                    label: 'Temperature (°C)',
                    data: tempData,
                    borderColor: '#4caf50', // Green
                    fill: true,
                    backgroundColor: 'rgba(76, 175, 80, 0.2)',
                }]
            }
        });

        // Update the graph with new data
        function updateGraph() {
            const temp = Math.random() * 10 + 22; // Generate random temperature
            tempData.push(temp);
            tempData.shift(); // Remove the oldest data point
            tempChart.update();
        }

        setInterval(updateGraph, 5000); // Update graph every 5 seconds
    </script>
</body>
</html>
