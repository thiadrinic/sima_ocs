import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Base } from "./pages/Base";
import { HardwareListado } from "./components/HardwareListado";
import { Equipo } from "./pages/Equipo";
import { Servicios } from "./pages/Servicios";
import { Repuestos } from "./pages/Repuestos";
import { Mantenimiento } from "./pages/Mantenimiento";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Base />}>
          <Route index element={<HardwareListado />} />
          <Route path="/equipo/:id" element={<Equipo />} />
          <Route path="/servicios" element={<Servicios />} />
          <Route path="/repuestos" element={<Repuestos />} />
          <Route path="/mantenimiento" element={<Mantenimiento />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
