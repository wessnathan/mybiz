
const url = window.location.href;
const searchForm = document.getElementById('searchForm')
const searchInput = document.getElementById('searchbar')
const searchResult = document.getElementById('searchResult')
const matchedResult = document.getElementById('matchedResults')
const defaultViews = document.getElementById('tp')
const searchReturned = document.getElementById('matched-search-results')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

let altSearch = document.querySelectorAll('.card-body')
console.log(altSearch);


const sendSearchData = (biz) => {
    $.ajax({
        type: 'POST',
        url: 'search/',
        data: {
            'csrfmiddlewaretoken':csrftoken,
            'biz':biz,
        },
        success: (res) => {
            console.log(res.data)
            const data = res.data
            if (Array.isArray(data)) {
                matchedResult.innerHTML = " ";
                data.forEach(biz => {
                    matchedResult.innerHTML += `
                    <div class="border col-8 mt-2 rounded px-2">
                            <div class="py-3 pt-1">
                                <a class="a-col text-left pt-2 text-secondary biz-head " href="${biz.username}">Username: ${biz.username}</a>
                                <p class="text-left">Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eveniet quidem tempore consequuntur voluptatem veritatis cum, ut repellat illo blanditiis at.</p>
                                <div class="d-flex flex-row-reverse flex-wrap text-left mb-auto" >
                                    <li class="list-unstyled rounded mt-1  px-1"><a href="${ biz.username}" class="d-flex-row mx-1"><i class="text-success fa fa-envelope fa-search " aria-hidden="true"></i>${biz.email}</a></li>
                                </div>
                            </div>
                            
                    </div>
                    `
                })
            } else {
                if (searchInput.value.length > 0) {
                    matchedResult.innerHTML = `<p>${data}</p>`;
                } else {
                    defaultViews.classList.remove('result-view-content');
                    //matchedResult.classList.toggle('result-view-content')
                    console.log(defaultViews);
                    console.log(matchedResult);
                }
            }
        },
        error: (err) => {
            console.log(err)
        }
        
    })
}


searchInput.addEventListener('keyup', e => {
    console.log(e.target.value);
    
    if (defaultViews.length !== 0) {
        defaultViews.classList.toggle('result-view-content');
        sendSearchData(e.target.value)
    } else {
        console.log('it worked')
    }
    
    
})