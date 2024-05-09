import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

import Equipo_pagina from "../components/Equipo_pagina";
import Equipo_Botones from "../components/Equipo_botones";

export function Equipo() {
  const { id } = useParams();
  const [equipo, setEquipo] = useState(null);
  useEffect(() => {
    async function fetchEquipo() {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/equipos/api/equipos/${id}`);
        setEquipo(response.data);
      } catch (error) {
        console.error("Error fetching equipo:", error);
      }
    }
    fetchEquipo();
  },[id]);

  if (!equipo) {
    return <div>Cargando...</div>;
  }

  return (
    <>
      <div className="w-full py-10">
        <div className="container mx-auto px-6 flex items-start justify-center">
          <div className="w-full">
            {/* Card is full width. Use in 12 col grid for best view. */}
            {/* Card code block start */}
            <div className="mx-auto w-full p-5 lg:p-10 bg-white dark:bg-gray-800 shadow rounded">
              <div className="flex flex-col lg:flex-row items-start lg:items-center mb-8">
                <h1 className="mr-12 text-xl lg:text-2xl text-gray-800 dark:text-gray-100 font-bold lg:w-1/2">
                  {equipo.Nombre}
                </h1>
                <div className="flex flex-col md:flex-row items-start md:items-center"></div>
              </div>
             <div className="flex justify-between">
             <div className="flex flex-col lg:flex-row items-start lg:items-center">
                <div className="w-full lg:w-1/2 pr-0 lg:pr-48">
                  <div className="flex items-center">
                    <div className="ml-2">
                      <h2 className="text-green-900 text-lg font" >
                        Modelo: {equipo.smodel}
                      </h2>
                      <h3 className="text-gray-600 dark:text-gray-400 text-s font-normal">
                        Tipo        : {equipo.tipo}<br />
                        Serie       : {equipo.ssn}<br />  
                        Mac Address : {equipo.MACADDR}<br />
                        IP          : {equipo.IPADDRESS}
                      </h3>
                    </div>
                  </div>
                  <p className="mt-5 text-sm text-w font-normal">
                    The web has witnessed mammoth advances; however a website’s
                    success still depends on just one thing: how users interact
                    with it.
                  </p>
                </div>
                <div className="lg:pl-8 w-full lg:w-1/2 flex flex-col lg:flex-row items-start lg:items-center">
                  <div className="mt-5 flex lg:block lg:mt-0">
                    <h2 className="text-gray-600 dark:text-gray-400 font-bold text-xl lg:text-2xl leading-6 mb-1 lg:text-center"></h2>
                  </div>
                </div>
              </div>
              <div className="flex flex-col gap-4 items-center">
                <div className="mt-4  text-sm bg-red-100 text-red-500 rounded font-medium py-2  flex justify-center w-[150px]">
                  Semaforo
                </div>
                <Equipo_Botones />
              </div>
             </div>
              <div className="relative">
                <hr className="absolute top-0 h-1 w-2/3 rounded bg-indigo-600" />
              </div>
              <div className="flex flex-col lg:flex-row items-start lg:items-center">
                <Equipo_pagina equipo={equipo} />
              </div>
            </div>
            {/* Card code block end */}
          </div>
        </div>
      </div>
    </>
  );
}
