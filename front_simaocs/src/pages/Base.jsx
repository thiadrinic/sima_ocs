import React, { useState } from "react";
import { HardwareListado } from "../components/HardwareListado";
export function Base() {
  const [show, setShow] = useState(false);
  const [product, setProduct] = useState(false);
  const [deliverables, setDeliverables] = useState(false);
  const [profile, setProfile] = useState(false);
  return (
    <>
      <div className="bg-gray-200 pb-10">
        {/* Navigation starts */}
        <nav className="w-full mx-auto bg-white shadow relative z-20">
          <div className="justify-between container px-6 h-16 flex items-center lg:items-stretch mx-auto">
            <div className="flex items-center">
              <div className="mr-10 flex items-center">
                <h3 className="text-base text-gray-800 font-bold tracking-normal leading-tight ml-3 hidden lg:block">
                  SimaOCS-URP
                </h3>
              </div>
              <ul className="pr-32 xl:flex hidden items-center h-full">
                <li className="hover:text-indigo-700 cursor-pointer h-full flex items-center text-sm text-indigo-700 tracking-normal">
                  Equipos / Laptops
                </li>
                <li className="hover:text-indigo-700 cursor-pointer h-full flex items-center text-sm text-gry-800 mx-10 tracking-normal relative">
                  Impresoras
                </li>
                <li className="hover:text-indigo-700 cursor-pointer h-full flex items-center text-sm text-gry-800 mr-10 tracking-normal">
                  Telefonia
                </li>
                <li className="hover:text-indigo-700 cursor-pointer h-full flex items-center text-sm text-gray-800 tracking-normal relative">
                  Otros
                </li>
              </ul>
            </div>
            <div className="h-full xl:flex hidden items-center justify-end">
              <div className="h-full flex items-center">
                <div className="w-32 pr-16 h-full flex items-center justify-end border-r" />
                <div className="w-full h-full flex">
                  <div className="w-16 xl:w-32 h-full flex items-center justify-center xl:border-r">
                    <div className="relative">
                      <div className="cursor-pointer w-6 h-6 xl:w-auto xl:h-auto text-gray-600">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          className="icon icon-tabler icon-tabler-bell"
                          width={28}
                          height={28}
                          viewBox="0 0 24 24"
                          strokeWidth={1}
                          stroke="currentColor"
                          fill="none"
                          strokeLinecap="round"
                          strokeLinejoin="round"
                        >
                          <path stroke="none" d="M0 0h24v24H0z" />
                          <path d="M10 5a2 2 0 0 1 4 0a7 7 0 0 1 4 6v3a4 4 0 0 0 2 3h-16a4 4 0 0 0 2 -3v-3a7 7 0 0 1 4 -6" />
                          <path d="M9 17v1a3 3 0 0 0 6 0v-1" />
                        </svg>
                      </div>
                      <div className="animate-ping w-2 h-2 rounded-full bg-red-400 border border-white absolute inset-0 mt-1 mr-1 m-auto" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </nav>
        {/* Navigation ends */}
        {/* Page title starts */}
        <div className="bg-gray-800 pt-8 pb-16 relative z-10">
          <div className="container px-6 mx-auto flex flex-col lg:flex-row items-start lg:items-center justify-between">
            <div className="flex-col flex lg:flex-row items-start lg:items-center">
              <div className="ml-0 lg:ml-20 my-6 lg:my-0">
                <h4 className="text-2xl font-bold leading-tight text-white mb-2">
                  Equipos / Laptops
                </h4>
                <p className="flex items-center text-gray-300 text-xs">
                  <span>Listado de Equipos</span>
                </p>
              </div>
            </div>
          </div>
        </div>
        {/* Page title ends */}
        <div className="container px-6 mx-auto">
          {/* Remove class [ h-64 ] when adding a card block */}
          <div className="rounded shadow relative bg-white z-10 -mt-8 mb-8 w-full h-64">
            {
              /* Place your content here */
              <HardwareListado></HardwareListado>
            }
          </div>
        </div>
      </div>
    </>
  );
}
