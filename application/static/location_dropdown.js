const state = document.getElementById('state');
const container = document.getElementById('locations');
const selectElementPropType = document.getElementById('property_type');


const states = {'CA' : ['San Diego', 'San Francisco', 'Los Angeles','San Mateo County', 'Oakland',
                      'Santa Cruz County', 'Pacific Grove'],   
                'NY' : ['New York City'],  
                'HI' : ['Anywhere in Hawaii'],   
                'MA' : ['Cambridge', 'Boston'],  
                'NV' : ['Clark County'],
                'DC' : ['Washington, D.C.'],   
                'IL' : ['Chicago'],   
                'LA' : ['New Orleans'],    
                'TN' : ['Nashville'],   
                'TX' : ['Austin'],   
                'WA' : ['Seattle'],    
                'MN' : ['Twin Cities'],    
                'OR' : ['Portland', 'Salem'],    
                'CO' : ['Denver'],    
                'RI' : ['Any City in Rhode Island'],    
                'NC' : ['Asheville'],    
                'NJ' : ['Jersey City'],    
                'OH' : ['Columbus'],    
                'FL' : ['Broward County']}

function make_dropdown(){
    var newDropdown = document.createElement('select');
    newDropdown.name = 'location';
    newDropdown.className = 'custom-select';
    newDropdown.id = 'location';
    newDropdown.innerHTML = `<option selected>${states[state.value][0]}</option>`;
    
    for (i = 1; i < states[state.value].length; i++) {
        var option = document.createElement('option');
        option.value = states[state.value][i];
        option.innerText = states[state.value][i];
        newDropdown.append(option);
      }  
    return newDropdown;
}

container.insertBefore(make_dropdown(), selectElementPropType);

state.addEventListener('change', (event) => {
    document.getElementById('location').replaceWith(make_dropdown());  
});
