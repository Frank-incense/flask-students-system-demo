import { createBrowserRouter } from 'react-router-dom'
import Layout from './components/Layout'
import Students from './pages/StudentPage'
import Courses from './pages/CoursesPage'
import Enrollments from './pages/EnrollmentsPage'

export const router = createBrowserRouter([
  {
    path: '/',
    element: <Layout />,
    children: [
      { path: '/students', element: <Students /> },
      { path: '/courses', element: <Courses/>},
      { path: '/enrollments', element: <Enrollments/>}
    ],
  },
])
