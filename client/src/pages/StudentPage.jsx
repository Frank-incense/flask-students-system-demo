import { useEffect, useState } from "react"
import Register from "../components/Registerform"
import Table from "../components/Table"

function Students(){
    const [students, setStudents] = useState([])
    useEffect(()=>{
        fetch('http://127.0.0.1:5555/students')
        .then(r => r.json())
        .then(data => {
            setStudents(data)
            print(data)
        })
    }, [])

    return(
    <>
        <Register display={'students'}/>
        <Table display={'students'} data={students}/>
    </>)
}

export default Students 