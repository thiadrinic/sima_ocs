import React from "react";
function Equipo_Botones() {
    return (
        <>
            <div className="px-6 flex flex-wrap">
                {/* Code block for white alternative button starts */}
                <p>
                <button className="mx-2 my-2 bg-white transition duration-150 ease-in-out hover:border-gray-900 hover:text-gray-900 rounded border border-gray-800 text-gray-800 px-6 py-2 text-xs">Servicios</button>
                {/* Code block for white alternative button ends */}
                {/* Code block for button with black outline starts */}
                </p><p>
                <button className="mx-2 my-2 bg-white transition duration-150 ease-in-out hover:border-gray-900 hover:text-gray-900 rounded border border-gray-800 text-gray-800 px-6 py-2 text-xs">Repuestos</button>
                {/* Code block for button with black outline ends */}
                {/* Code block for gray button starts */}
                </p><p>
                <button className="mx-2 my-2 bg-white transition duration-150 ease-in-out hover:border-gray-900 hover:text-gray-900 rounded border border-gray-800 text-gray-800 px-6 py-2 text-xs">Mantenimiento</button>
                {/* Code block for gray button ends */}
                {/* Code block for gray alternative button starts */}
                </p>
                <p>
                <button className="mmx-2 my-2 bg-white transition duration-150 ease-in-out hover:border-gray-900 hover:text-gray-900 rounded border border-gray-800 text-gray-800 px-6 py-2 text-xs">Hoja de Vida</button>
                {/* Code block for gray alternative button ends */}
                {/* Code block for button with gray outline starts */}
                </p>
            </div>
        </>
    );
}
export default Equipo_Botones;