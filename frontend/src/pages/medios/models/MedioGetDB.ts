export type MedioGetDB = {
    id : string;
    name: string;
    state: string;
    location: string;
    classroom_id: string;
    type: string;
};

export type MedioGetResponse = {
    [index: string]: MedioGetDB
}