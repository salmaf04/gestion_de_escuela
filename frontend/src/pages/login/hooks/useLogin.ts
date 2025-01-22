import {useContext, useState} from "react";
import api from "../api/loginRequests.ts";
import IGetTokenResponse from "../dto/IGetTokenResponse.ts";
import {AppContext} from "../../../App.tsx";

export const useLogin = () => {
    const [isLoading, setIsLoading] = useState(false)
    const isMocked = false;
    const {setError, setToken, token} = useContext(AppContext)


    const getToken = async (username: string, password: string) => {
        setIsLoading(true)
        if (isMocked) {
            setTimeout(() => {
                setToken!( 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZHJpYW4iLCJ0eXBlIjoidXNlciIsImV4cCI6MTczNzI3MzE0Nn0.AOLgvIgCq3BoGvLvzUFdoTsty_4m_xKnURCjkYB99Vg')
            }, 2000)
        }
        else {
            const res = await api.getToken(username, password)
            if (res.ok) {
                const data: IGetTokenResponse = await res.json()
                setToken!(data.access_token)
                sessionStorage.setItem('token', data?.access_token)
            } else {
                setError!(new Error(res.statusText))
            }
        }
        setIsLoading(false)

    }

    return {
        isLoading,
        token,
        getToken,
    }
}