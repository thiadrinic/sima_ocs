import axios from 'axios'

export const GetAllHardware = () => {
    return axios.get('http://127.0.0.1:8000/hardware/api/hardware/')
}