import { useEffect } from 'react';
import { GetAllHardware } from '../api/Hardware'
import axios from 'axios'


export function HardwareListado() {
    console.log('Hola mundo')
     useEffect(()=> {
         async function loadHardware() {
            const lst = await axios.get("http://127.0.0.1:8000/hardware/api/hardware/");
            console.log(lst);
            }
        loadHardware();
        }, []);

    return <div>Listado de Equipos</div>;
    }