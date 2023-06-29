console.clear()
console.info((new Date()).toUTCString(),'\n')

const url="https://www.amazon.in/dp/B0C4T91SNK?linkCode=sl1&th=1&psc=1&tag=ozians06-21"
const delete_params=["tag","ref","ref_","red"]

function process_url(url){
    let new_url=''
    let url_parts = url.split('?')
    url_parts = [url_parts[0],...url_parts[1].split('&')]

    for (const url_part of url_parts) {
        let parts = url_part.split('=')
        if(parts.length > 1 && delete_params.includes(parts[0])){
            continue
        }
        else{
            new_url+=url_part
        }
    }


    return new_url
}

console.log(
    process_url(url)
)

`
https://www.amazon.in/b?ie=UTF8&node=77323998031&ref=ebd
https://www.amazon.in/s?k=menhood+grooming+trimmer&red=ebd&sprefix=menhood+%2Caps%2C1448&ref=ebd
https://www.amazon.in/deal/9641fee6?showVariations=true&ref_=cm_sw_r_api_dlpg_oH7y7fmMLOV3q&ref=ebd
https://www.amazon.in/dp/B076Q1NVQV/ref=ebd
https://www.amazon.in/s?me=A1SU155JFG0BDG&marketplaceID=A21TJRUUN4KGV&ref=ebd
https://www.amazon.in/dp/B0C4T91SNK?linkCode=sl1&th=1&psc=1&tag=ozians06-21
https://www.amazon.in/dp/B0C4T91SNK?linkCode=sl1&th=1&psc=1&tag=ozians06-21&tat=1
`