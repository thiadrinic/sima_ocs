import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

export function Equipo_periferico({ equipo }) {
  const [Periferico, setPeriferico] = useState([]);
  useEffect(() => {
    async function loadPeriferico() {
      const { data } = await axios.get(
        `http://127.0.0.1:8000/equipos/api/perifericos/${equipo.id}`
      );

      const data2 = await axios.get(
        `http://127.0.0.1:8000/equipos/api/perifericos/`
      );

      const filterPeriferico = data2.data.filter(
        (perifericos) => perifericos.equipo_id == data.equipo_id
      );
      setPeriferico(filterPeriferico);
    }
    loadPeriferico();
  }, []);
  return (
    <>
      <div className="w-full max-w-2xl px-4">
        <div className="rounded-lg border pb-6 border-gray-200">
          <div className="flex items-center border-b border-gray-200 justify-between px-6 py-3">
            <p className="text-sm lg:text-xl font-semibold leading-tight text-gray-800">
              Perifericos Activos
            </p>
            <div className="flex cursor-pointer items-center justify-center px-3 py-2.5 border rounded border-gray-100">
              <p className="text-xs md:text-sm leading-none text-gray-600">
                Boton de Nuevo Periferico
              </p>
            </div>
          </div>
          <div className="px-6 pt-6 overflow-x-auto">
            <table className="w-full whitespace-nowrap">
              <tbody>
                {Periferico.map((data2, index) => (
                  <tr key={index}>
                    <td>
                      <div className="flex items-center">
                        <div className="bg-gray-100 rounded-sm p-2.5">
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            viewBox="0 0 24 24"
                            width="24"
                            height="24"
                            fill="none"
                          >
                            <path
                              d="M12 1c-5.52 0-10 4.48-10 10s4.48 10 10 10 10-4.48 10-10-4.48-10-10-10zm0 2c4.42 0 8 3.58 8 8s-3.58 8-8 8-8-3.58-8-8 3.58-8 8-8z"
                              fill="#6B7280"
                            />
                            <path
                              d="M13 17.5c-.28 0-.5-.22-.5-.5s.22-.5.5-.5h3.5v-2h-5.5c-.28 0-.5-.22-.5-.5s.22-.5.5-.5h5.5v-1c0-1.93-1.57-3.5-3.5-3.5s-3.5 1.57-3.5 3.5v1H6c-.28 0-.5.22-.5.5s.22.5.5.5h3.5v2H6c-.28 0-.5.22-.5.5s.22.5.5.5h1.73l-1.87 4.44c-.14.33-.05.71.21.95.26.23.64.27.95.08l1.66-1.05c.13-.08.28-.12.43-.12.23 0 .46.1.62.29l1.47 1.71c.22.26.59.3.85.08.26-.22.3-.59.08-.85l-1.3-1.51 1.94-4.59H13z"
                              fill="#6B7280"
                            />
                          </svg>
                        </div>
                        <div className="pl-3">
                          <div className="flex items-center text-sm leading-none">
                            <p className="font-semibold text-gray-800">
                              {(() => {
                                switch (data2.tipo_perif) {
                                  case "MN":
                                    return "MONITOR";
                                  case "TC":
                                    return "TECLADO";
                                  case "MS":
                                    return "MOUSE";
                                  default:
                                    return "";
                                }
                              })()}
                            </p>
                            <p className="text-blue-500 ml-3">
                              Serie: {data2.serie_perif}
                            </p>
                          </div>
                          <p className="text-xs md:text-sm leading-none text-gray-600 mt-2">
                            Marca: {data2.marca_perif} / Modelo:{" "}
                            {data2.modelo_perif}
                          </p>
                        </div>
                      </div>
                    </td>
                    <td className="pl-16">
                      <div>
                        <p className="text-sm font-semibold leading-none text-right text-gray-800">
                          Inventario: {data2.inventario_perif}
                        </p>
                        <div className="flex items-center justify-center px-2 py-1 mt-2 bg-green-100 rounded-full">
                          <p className="text-xs leading-3 text-green-700">
                            Censo
                          </p>
                        </div>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </>
  );
}
