export function getQueryParamsFromObject(obj: any): string {
    return "?"+ Object.keys(obj)
        .map(key => `${key}=${obj[key]}`)
        .join('&');

}