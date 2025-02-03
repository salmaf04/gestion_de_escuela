export type ProfesorDB = {

        id: string
        "name": string
        "lastname": string
        "specialty": string
        "contract_type": string
        "experience": number
        "salary" : number,
        "email": string
        "username": string
        "list_of_subjects": string[]
        "valoration": string,
        alert: number
    }

export type ProfesorGetResponse = ProfesorDB[]