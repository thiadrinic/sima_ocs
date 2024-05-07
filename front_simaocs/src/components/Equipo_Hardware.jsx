import React from "react";

function Equipo_Hardware({id_p}) {

    return (
        <>
            <div className="xl:w-3/4 2xl:w-4/5 w-full">
                <div className="px-4 md:px-10 py-4 md:py-7">
                    <div className="sm:flex items-center justify-between">
                        <p className="text-base sm:text-lg md:text-xl lg:text-2xl font-bold leading-normal text-gray-800">Hardware</p>
                        <div className="mt-4 sm:mt-0">
                            <button className="inline-flex sm:ml-3 items-start justify-start px-6 py-3 bg-indigo-700 hover:bg-indigo-600 focus:outline-none rounded">
                                <p className="text-sm font-medium leading-none text-white">Agregar Nuevo</p>
                            </button>
                        </div>
                    </div>
                </div>
                <div className="bg-white px-4 md:px-10 pb-5">
                    <div className="overflow-x-auto">
                        <table className="w-full whitespace-nowrap">
                            <tbody>
                                <tr className="text-sm leading-none text-gray-600 h-16">
                                    <td className="w-1/2">
                                        <div className="flex items-center">
                                            <div className="w-10 h-10 bg-gray-700 rounded-sm flex items-center justify-center">
                                                <p className="text-xs font-bold leading-3 text-white">MTH</p>
                                            </div>
                                            <div className="pl-2">
                                                <p className="text-sm font-medium leading-none text-gray-800">Motherboard</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td className="pl-16">
                                        <p>Variable {id_p}</p>
                                    </td>
                                </tr>
                                <tr className="text-sm leading-none text-gray-600 h-16">
                                    <td className="w-1/2">
                                        <div className="flex items-center">
                                            <div className="w-10 h-10 bg-cyan-700 rounded-sm flex items-center justify-center">
                                                <p className="text-xs font-bold leading-3 text-white">CPU</p>
                                            </div>
                                            <div className="pl-2">
                                                <p className="text-sm font-medium leading-none text-gray-800">Procesador</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td className="pl-16">
                                        <p>#designer</p>
                                    </td>
                                </tr>
                                <tr className="text-sm leading-none text-gray-600 h-16">
                                    <td className="w-1/2">
                                        <div className="flex items-center">
                                            <div className="w-10 h-10 bg-green-700 rounded-sm flex items-center justify-center">
                                                <p className="text-xs font-bold leading-3 text-white">HDD</p>
                                            </div>
                                            <div className="pl-2">
                                                <p className="text-sm font-medium leading-none text-gray-800">Disco Duro</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td className="pl-16">
                                        <p>#designer</p>
                                    </td>
                                </tr>
                                <tr className="text-sm leading-none text-gray-600 h-16">
                                    <td className="w-1/2">
                                        <div className="flex items-center">
                                            <div className="w-10 h-10 bg-yellow-700 rounded-sm flex items-center justify-center">
                                                <p className="text-xs font-bold leading-3 text-white">RAM</p>
                                            </div>
                                            <div className="pl-2">
                                                <p className="text-sm font-medium leading-none text-gray-800">Memoria</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td className="pl-16">
                                        <p>#designer</p>
                                    </td>
                                </tr>
                                <tr className="text-sm leading-none text-gray-600 h-16">
                                    <td className="w-1/2">
                                        <div className="flex items-center">
                                            <div className="w-10 h-10 bg-red-700 rounded-sm flex items-center justify-center">
                                                <p className="text-xs font-bold leading-3 text-white">GPU</p>
                                            </div>
                                            <div className="pl-2">
                                                <p className="text-sm font-medium leading-none text-gray-800">Tarjeta Grafica</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td className="pl-16">
                                        <p>#designer</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </>
    );
}

export default Equipo_Hardware;
