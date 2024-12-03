interface layoutProps
{
    name : string
}



function Layout({name} : layoutProps) {
    return (

        <div className={'h-svh bg-indigo-50'}>
            <div className={'w-full px-10 h-32 flex items-center'}>
                <div className={'flex flex-col content-center w-56'}>
                    <h1 className={'text-2xl text-indigo-400 start-0'}>Bienvenida</h1>
                    <h2 className={'text-xl text-end'}>{name}</h2>
                </div>
            </div>
            <div className={'flex'}>
                <div className={'w-1/6 flex flex-col justify-center items-center'}>
                    <div className={' flex flex-col items-center justify-center gap-10'}>
                        //Menu
                    </div>
                </div>
                <div className={'mx-4 w-5/6 flex flex-col'}>
                    <div className={'flex-wrap flex items-center justify-around w-full h-28'}>
                        //Header
                    </div>
                    <div>
                        //Table
                    </div>

                </div>
            </div>
        </div>
    )
}

export default Layout