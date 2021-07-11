import axios from "axios";
import {dummyData} from "../dummy.json"


const UseSolver = () => {

  const deserializeData = (data) => {
    data.vehicles = data.vehicles.map((vehicle, index) => {
      return {...vehicle, id: index + 1, capacity: [vehicle.capacity]}
    })
    data.jobs = data.jobs.map((job, index) => {
      return {...job, id: index + 1, delivery: [job.delivery]}
    })
    if (Object.keys(data).includes("matrix")) {
      data.matrix = JSON.parse(data.matrix)
    } else {
      data.matrix = dummyData.matrix
    }
    return data
  }


  const solve = async (data) => {
    try {
      const {data: resultData} = await axios.post("http://localhost:8000/solve", deserializeData(data))
      return resultData
    } catch (error) {
      return error
    }
  }

  return {
    solve
  }
};

export default UseSolver;
