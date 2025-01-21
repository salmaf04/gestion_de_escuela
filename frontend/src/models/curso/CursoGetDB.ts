export type CursoGetDB = {
    id : string ;
    start_year: string ;
    end_year: string ;
};

export type CursoGetResponse = {
    [index: string]: CursoGetDB
}