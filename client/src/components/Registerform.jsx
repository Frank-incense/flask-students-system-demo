import { useState } from "react"

function Register({display}){
    const [register, setRegister] = useState(display)
    if (register === 'students'){
        return (
        <form>
            <div className="mb-3">
                <label htmlFor="name" className="form-label">Name:</label>
                <input type="name" className="form-control" id="name" aria-describedby="nameHelp"/>
                <div id="nameHelp" className="form-text">We'll never share your name with anyone else.</div>
            </div>
            <div className="mb-3">
                <label htmlFor="age" className="form-label">Age</label>
                <input type="number" className="form-control" id="age"/>
            </div>
        </form>)
        }
        else if (register === 'courses'){
        return (
        <form>
            <div className="mb-3">
                <label htmlFor="name" className="form-label">Name:</label>
                <input type="name" className="form-control" id="name" aria-describedby="nameHelp"/>
                <div id="nameHelp" className="form-text">We'll never share your name with anyone else.</div>
            </div>
            <div className="mb-3">
                <label htmlFor="age" className="form-label">Age</label>
                <input type="number" className="form-control" id="age"/>
            </div>
        </form>)
        }
 
}

export default Register