import ScreenType, {Screens} from "../types.ts";

interface Props {
    actualScreen: ScreenType,
    setActualScreen: (screen: ScreenType) => void
}

function Sidebar({actualScreen, setActualScreen}: Props) {
    return <div className={"w-1/12 h-full flex items-center"}>
        <div className={'flex flex-col items-center justify-center h-full'}>
            {
                Object.values(Screens).map((screen: ScreenType) => {
                    return (
                        <div key={screen.title} onClick={() => setActualScreen(screen)}
                             className={`transition-all cursor-pointer font-semibold px-3 size-full space-y-1 justify-center rounded-xl flex flex-col items-center ${actualScreen === screen ? 'bg-indigo-100' : ''}`}>
                            <img src={screen.icon} alt={screen.title}/>
                            <p className={'text-xs text-indigo-950'}>{screen.title}</p>
                        </div>)
                })
            }

        </div>
    </div>;
}

export default Sidebar