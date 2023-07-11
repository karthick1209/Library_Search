import React, { useEffect, useState } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

const LibraryView = () => {
    const [lib, setLib] = useState([]);
    const [search, setSearch] = useState('');
    const [selectedHeading, setSelectedHeading] = useState('');

    useEffect(() => {
        fetchData();
    }, []);

    const fetchData = async() => {
        try {
            const response = await fetch('http://127.0.0.1:8000/retrive_view/');
            const data = await response.json();
            setLib(data);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    const handleHeadingChange = (e) => {
        setSelectedHeading(e.target.value);
    };

    const handleSearchChange = (e) => {
        setSearch(e.target.value);
    };

    const filteredData = lib.filter((data) => {
        if (!selectedHeading) return true;

        const searchData = data[selectedHeading].toString().toLowerCase() || '';
        return searchData.includes(search.toLowerCase());
    });

    const tableHeadings = Object.keys(lib[0] || {}).filter(heading => heading !== 'available' && heading !== 'id');

    return ( <
            div className = "container" >
            <
            div className = "row" >
            <
            div className = "col-md-4 mb-3" >
            <
            label htmlFor = "heading-select" > Select Heading: < /label> <
            select id = "heading-select"
            className = "form-select"
            value = { selectedHeading }
            onChange = { handleHeadingChange } >
            <
            option value = "" > All < /option> {
            tableHeadings.map((heading, index) => ( <
                option key = { index }
                value = { heading } > { heading } <
                /option>
            ))
        } <
        /select> < /
    div > <
        div className = "col-md-4 mb-3" >
        <
        label htmlFor = "search-input" > Search: < /label> <
    input id = "search-input"
    type = "text"
    className = "form-control"
    placeholder = "Enter search query"
    value = { search }
    onChange = { handleSearchChange }
    /> < /
    div > <
        /div>

    <
    table className = "table table-striped" >
        <
        thead >
        <
        tr > {
            tableHeadings.map((heading, index) => ( <
                th key = { index } > { heading } < /th>
            ))
        } <
        /tr> < /
    thead > <
        tbody > {
            filteredData.map((data, index) => ( <
                tr key = { index } > {
                    tableHeadings.map((heading, index) => ( <
                        td key = { index } > { data[heading] } < /td>
                    ))
                } <
                /tr>
            ))
        } <
        /tbody> < /
    table > <
        /div>
);
};

export default LibraryView;