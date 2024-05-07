import React from "react";
import { Link } from "react-router-dom";

function Equipo_Botones() {
  return (
    <>
      <div className="px-6 flex flex-col">
        {/* Code block for white alternative button starts */}
        <p>
          <Link to="/servicios">
            <button className="mx-2 my-2 bg-white transition duration-150 ease-in-out hover:border-gray-900  rounded border border-gray-800 text-gray-800 px-6 py-2 text-xs w-[150px] hover:bg-green-800 hover:text-white hover:font-bold">
              Servicios
            </button>
          </Link>
          {/* Code block for white alternative button ends */}
          {/* Code block for button with black outline starts */}
        </p>
        <p>
        <Link to="/repuestos">
          <button className="mx-2 my-2 bg-white transition duration-150 ease-in-out hover:border-gray-900  rounded border border-gray-800 text-gray-800 px-6 py-2 text-xs w-[150px] hover:bg-green-800 hover:text-white hover:font-bold">
            Repuestos
          </button>
          </Link>
          {/* Code block for button with black outline ends */}
          {/* Code block for gray button starts */}
        </p>
        <p>
        <Link to="/mantenimiento">
          <button className="mx-2 my-2 bg-white transition duration-150 ease-in-out hover:border-gray-900  rounded border border-gray-800 text-gray-800 px-6 py-2 text-xs w-[150px] hover:bg-green-800 hover:text-white hover:font-bold">
            Mantenimiento
          </button>
          </Link>
          {/* Code block for gray button ends */}
          {/* Code block for gray alternative button starts */}
        </p>
        <p>
          <button className="mx-2 my-2 bg-white transition duration-150 ease-in-out hover:border-gray-900  rounded border border-gray-800 text-gray-800 px-6 py-2 text-xs w-[150px] hover:bg-green-800 hover:text-white hover:font-bold">
            Hoja de Vida
          </button>
          {/* Code block for gray alternative button ends */}
          {/* Code block for button with gray outline starts */}
        </p>
      </div>
    </>
  );
}
export default Equipo_Botones;
