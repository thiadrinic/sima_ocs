import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Base } from "./pages/Base";
import { HardwareListado } from "./components/HardwareListado";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/Base" element={<Base />} />

        <Route path="/Listar" element={<HardwareListado />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
