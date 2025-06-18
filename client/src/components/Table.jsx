
function Table({display, data}){
    console.log(data)
    if (display === 'students'){
      return (
        <table className="table">
            <thead>
                <tr>
                <th scope="col">id</th>
                <th scope="col">name</th>
                <th scope="col">age</th>
                <th></th>
                </tr>
            </thead>
            <tbody>
                {data.map((d)=>{
                    return(<tr key={d.id}>
                        <td>{d.id}</td>
                        <td>{d.name}</td>
                        <td>{d.age}</td>
                        <td></td>
                    </tr>)
                })}
                
            </tbody>
        </table>
    )  
    }
    
}

export default Table