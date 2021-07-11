# Capacitated Vehicle Routing Problem - Sample
## About The Project

In the project, route calculations can be made according to the number of vehicles and work locations using the or-tools library. In addition, a web interface has been created with React to easily try this.

### Built with

* FastApi
* React
* Google OR-Tools

## Installation
### Manual

```sh
git clone https://github.com/resulyrt93/vrp_project.git
cd vrp_project
pip install -r requirements.txt
cd src/
uvicorn main:app --reload
```

Also you can build React app on your local. 

```sh
cd frontend/
yarn install
yarn serve
```

### Docker

You can easily get the project up and running using Docker. All you need to do is run the following commands.

```sh
git clone https://github.com/resulyrt93/vrp_project.git
cd vrp_project
docker-compose up
```

## Usage

Backend is served on 8000 port, frontend is served on 3000 port. You can put a healthcheck request to API with ```localhost:8000/check``` endpoint. 
You can also make a post request to ```localhost:8000/solve``` for solve routing problem. Request data structure explained below.
```json
{
  "vehicles": [
    {
      "id": 1,
      "start_index": 0,
      "capacity": [
        4
      ]
    }
  ],
  "jobs": [
    {
      "id": 1,
      "location_index": 3,
      "delivery": [
        2
      ],
      "service": 327
    },
    {
      "id": 2,
      "location_index": 4,
      "delivery": [
        1
      ],
      "service": 391
    }
  ],
  "matrix": [
    [0, 516, 226, 853, 1008, 1729, 346, 1353, 1554, 827],
    [548, 0, 474, 1292, 1442, 2170, 373, 1801, 1989, 1068],
    [428, 466, 0, 1103, 1175, 1998, 226, 1561, 1715, 947],
    [663, 1119, 753, 0, 350, 1063, 901, 681, 814, 1111],
    [906, 1395, 1003, 292, 0, 822, 1058, 479, 600, 1518],
    [1488, 1994, 1591, 905, 776, 0, 1746, 603, 405, 1676],
    [521, 357, 226, 1095, 1167, 1987, 0, 1552, 1705, 1051],
    [1092, 1590, 1191, 609, 485, 627, 1353, 0, 422, 1583],
    [1334, 1843, 1436, 734, 609, 396, 1562, 421, 0, 1745],
    [858, 1186, 864, 1042, 1229, 1879, 984, 1525, 1759, 0]
  ]
}
```
