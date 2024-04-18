import {useState, useEffect} from "react"
import { useOutletContext, useNavigate } from "react-router-dom";

function NewBookingForm(){

    const [formData, setFormData] = useState({
        price: 0.0,
        destination: ""
    })

    const {flights, addBooking} = useOutletContext()
    const navigate = useNavigate()

    useEffect(() => {
        if(flights.length > 0){
            setFormData({...formData, flight_id: flights[0].id})
        }
    }, [flights])

    const optionsElements = flights.map(flight => {
        return <option key={flight.id} value={flight.id}>{flight.id}: {flight.airline}</option>
    })

    function updateFormData(event){
        if(event.target.name === 'price' || event.target.name == "flight_id"){
            setFormData({...formData, [event.target.name]: Number(event.target.value)})
        }
        else{
            setFormData({...formData, [event.target.name]: event.target.value})
        }
    }

    function handleSubmit(event){
        event.preventDefault()
        addBooking(formData)
        navigate('/bookings_list')
    }

    return (
        <>
            { flights.length > 0 ?
                <form onSubmit={handleSubmit}>
                <h1>Add New Booking</h1>
                <select onChange={updateFormData} name="flight_id">
                    {optionsElements}
                </select>
                <input onChange={updateFormData} type="number" name="price" placeholder="Price" value={formData.price}/>
                <input onChange={updateFormData} type="text" name="destination" placeholder="Destination" value={formData.destination}/>
                <input type="submit" value="Add Flight"/>
                </form> :
                <h1>Sorry, there are no Flights available.</h1>
            }
        </>
    )
}

export default NewBookingForm;