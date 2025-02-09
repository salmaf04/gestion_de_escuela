import {EndpointEnum} from "./EndpointEnum.ts";
import {IApiObject} from "./IApiObject.ts";


function postApi(endpoint: string, body: IApiObject, queryParams: string = "") {
    return fetch(`http://localhost:8000/${endpoint}${queryParams}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify(body),
    })
}

function getApi(endpoint: EndpointEnum, queryParams: string = "") {
    return fetch(`http://localhost:8000/${endpoint}${queryParams}`, {
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}
function getOneApi(endpoint: EndpointEnum, id: string) {
    return fetch(`http://localhost:8000/${endpoint}/${id}`, {
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}
//todo id path everybody
function patchApi(endpoint: EndpointEnum, id: string = "", body: IApiObject, queryParams: string = "") {
    return fetch(`http://localhost:8000/${endpoint}/${id}${queryParams}`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify(body),
    })
}

function deleteApi(endpoint: EndpointEnum, id: string, body: object = {}) {
    return fetch(`http://localhost:8000/${endpoint}/${id}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        },
        body: JSON.stringify(body),
    })
}

export default {getApi, postApi, deleteApi, patchApi, getOneApi}