import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

export function Equipo_software({ equipo }) {
  const [Software, setSoftware] = useState([]);
  useEffect(() => {
    async function loadSoftware() {
      const { data } = await axios.get(
        `http://127.0.0.1:8000/equipos/api/software/${equipo.id}`
      );

      const data2 = await axios.get(
        `http://127.0.0.1:8000/equipos/api/software/`
      );

      const filterSoftware = data2.data.filter(
        (software) => software.equipo_id == data.equipo_id
      );
      setSoftware(filterSoftware);
    }
    loadSoftware();
  }, []);
  return (
    <>
      <div className="py-20">
        <div className="mx-auto container bg-white dark:bg-gray-800 shadow rounded">
          <div className="w-full overflow-x-scroll xl:overflow-x-hidden">
            <table className="min-w-full bg-white dark:bg-gray-800">
              <thead>
                <tr className="w-full h-16 border-gray-300 dark:border-gray-200 border-b py-8">
                  <th className="text-gray-600 dark:text-gray-400 font-normal pr-6 text-left text-sm tracking-normal leading-4">
                    Invoice Number
                  </th>
                  <th className="text-gray-600 dark:text-gray-400 font-normal pr-6 text-left text-sm tracking-normal leading-4">
                    Client
                  </th>
                  <th className="text-gray-600 dark:text-gray-400 font-normal pr-6 text-left text-sm tracking-normal leading-4">
                    Company Contact
                  </th>
                </tr>
              </thead>
              <tbody>
                {Software.map((data2, index)=>(
                    <tr key={index} className="h-24 border-gray-300 dark:border-gray-200 border-b">
                  <td className="text-sm pr-6 whitespace-no-wrap text-gray-800 dark:text-gray-100 tracking-normal leading-4">
                    {data2.distribuidor}
                  </td>
                  <td className="text-sm pr-6 whitespace-no-wrap text-gray-800 dark:text-gray-100 tracking-normal leading-4">
                  {data2.software}
                  </td>
                  <td className="text-sm pr-6 whitespace-no-wrap text-gray-800 dark:text-gray-100 tracking-normal leading-4">
                  {data2.version}
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
