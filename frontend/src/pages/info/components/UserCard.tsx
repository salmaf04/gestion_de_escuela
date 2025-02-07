import UserIcon from "../../../assets/user.svg";



interface Props{
    data: UserDataProp[]
}
export interface UserDataProp {
    name: string,
    value: string
}
export default function UserCard({data}: Props){
    return (
        <div className={'flex flex-col space-y-5 items-center'}>
            <img src={UserIcon} alt={'usuario'} width={150}/>
            <div className={'flex flex-col space-y-1 items-center'}>
                {
                    data.map((item, index) => {
                        return (
                            <div key={index} className={'flex space-x-2'}>
                                <h2 className={'text-indigo-400'}>{item.name}:</h2>
                                <p className={'text-indigo-950 font-semibold'}>{item.value}</p>
                            </div>
                        )
                    })
                }
            </div>

        </div>
    )
}