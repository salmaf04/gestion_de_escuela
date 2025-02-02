export type ProfesorDB = {

        id: string
        "name": string
        "lastname": string
        "specialty": string
        "contract_type": string
        "experience": number
        "email": string
        "username": string
        "salary" : number,
        "list_of_subjects": string[]
        "valoration": string
    }

export type ProfesorGetResponse = ProfesorDB[]