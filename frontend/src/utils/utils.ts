export function getQueryParamsFromObject(obj: any): string {
    return "?"+ Object.keys(obj)
        .map(key => `${key}=${obj[key]}`)
        .join('&');
}
export function reverseDate(date: string): string {
    return date.split('-').reverse().join('-')
}