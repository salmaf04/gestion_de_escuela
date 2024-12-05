import Navbar from "./components/Navbar.tsx";
import Sidebar from "./components/Sidebar.tsx";
import Content from "./components/Content.tsx";
import {useState} from "react";
import AddForm from "./components/AddForm.tsx";
import {data} from "./components/Example_data.tsx";


interface Props
{
    name : string
}


const Data = data;



export default function LayoutScreen({name} : Props) {
    const [isAddFormVisible, setIsAddFormVisible] = useState(false);

    const [data, setData] = useState(Data);

    const handleAddButtonClick = () => {
        setIsAddFormVisible(true);
    };

    const [index ,setIndex] = useState(0)

    const handleCloseAddForm = (IsEdit : boolean) => {
        if(IsEdit){setEdit(false)}
        setIsAddFormVisible(false);
    };

    const handleEdit = (index:number) => {
        handleAddButtonClick()
        setEdit(true)
        setIndex(index)
    }
    const [edit,setEdit] = useState(false)



    return (

        <div className={' bg-indigo-50'}>
            {isAddFormVisible && <AddForm Index={index}  Data={Data} IsEdit={edit} onClose={handleCloseAddForm} />}
            <Navbar name={name}/>
            <div className={'flex'}>
                <Sidebar/>
                <Content Data={Data}  setEdit={handleEdit} setFormVisible={handleAddButtonClick}/>
            </div>
        </div>
    )
}
