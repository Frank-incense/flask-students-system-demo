import { useState } from 'react'
import './App.css'
import NavBar from './components/Navbar'
import Table from './components/Table'
import Register from './components/Registerform'
import { RouterProvider } from 'react-router-dom'
import Students from './pages/StudentPage'
import { router } from './routes'


function App() {
  return (
    <>
      
      <RouterProvider router={router}/>
      {/* <BrowserRouter>
        <Routes>
          <Route path='/students' element={<Students/>}/>
        </Routes>
      </BrowserRouter> */}
    </>
   
   
  )
}

export default App
