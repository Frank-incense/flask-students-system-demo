
import { Outlet } from 'react-router-dom'
import NavBar from './Navbar'

export default function Layout() {
  return (
    <>
      <NavBar />
      <Outlet /> {/* This is where nested components will be rendered */}
    </>
  )
}
