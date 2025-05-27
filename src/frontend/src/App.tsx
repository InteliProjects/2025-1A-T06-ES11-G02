import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import LoginPage from "../app/page"
import DashboardPage from "../app/dashboard/page"
import DataPage from "../app/data/page"

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/data" element={<DataPage />} />
      </Routes>
    </Router>
  )
}

export default App

