
import ScreenType from "../types.ts";

interface props{
    actualScreen: ScreenType
}

function Content({actualScreen}: props) {
    return(
        <>
            {actualScreen.screen}
        </>
    )


}

export default Content