export type AulaGetDB = {
    id : string ;
    location: string;
    capacity: number;
};

export type AulaGetResponse = {
    [index: string]: AulaGetDB
}