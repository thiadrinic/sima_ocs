import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Base } from "./pages/Base";
import { HardwareListado } from "./components/HardwareListado";
import { Equipo } from "./pages/Equipo";
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/Base" element={<Base />} />
        <Route path="/equipos" element={<HardwareListado />} />
        <Route path="/equipo" element={<Equipo />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
