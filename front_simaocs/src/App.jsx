import  {BrowserRouter, Routes,Route} from 'react-router-dom'
import { Hardware } from './pages/Hardware'
import { HardwareListado } from './components/HardwareListado'

function App() {

  return (
    <BrowserRouter>
        <Routes>
            <Route path="/Listado" element={<Hardware />} />
             <Route path="/Listar" element={<HardwareListado />} />
        </Routes>
    </BrowserRouter>

  )
}

export default App
