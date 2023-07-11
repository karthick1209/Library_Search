import React, { useEffect, useState } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Select from 'react-select';

const LibraryView = () => {
    const [lib, setLib] = useState([]);
    const [search, setSearch] = useState('');
    const [selectedHeadings, setSelectedHeadings] = useState([]);
    const [headingOptions, setHeadingOptions] = useState([]);

    useEffect(() => {
        fetchData();
    }, []);

    useEffect(() => {
        const options = getHeadingOptions();
        setHeadingOptions(options);
    }, [lib]);

    const fetchData = async() => {
        try {
            const response = await fetch('http://127.0.0.1:8000/retrive_view/');
            const data = await response.json();
            setLib(data);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    const getHeadingOptions = () => {
        const headings = Object.keys(lib[0] || {});
        return headings.map((heading) => ({
            value: heading,
            label: heading,
        }));
    };

    const handleHeadingChange = (selectedOptions) => {
        const selectedHeadings = selectedOptions.map((option) => option.value);
        setSelectedHeadings(selectedHeadings);
    };

    const handleSearchChange = (e) => {
        setSearch(e.target.value);
    };

    const filteredData = lib.filter((data) => {
        const searchData = selectedHeadings.flatMap((heading) => {
            const value = Object.values(data[heading]).join(' ').toLowerCase();
            return heading.includes(search.toLowerCase()) ? [value] : [];
        });
        return searchData.length > 0;
    });

    return ( <
        div className = "container" >
        <
        div className = "row" >
        <
        div className = "col-md-6 mb-3" >
        <
        Select isMulti options = { headingOptions }
        onChange = { handleHeadingChange }
        placeholder = "Select Headings" /
        >
        <
        /div> <
        div className = "col-md-6 mb-3" >
        <
        input type = "text"
        className = "form-control"
        placeholder = "Search"
        value = { search }
        onChange = { handleSearchChange }
        /> <
        /div> <
        /div>

        <
        table className = "table table-striped" >
        <
        thead >
        <
        tr >
        <
        th > Book Title < /th> <
        th > Author < /th> <
        th > Publication Date < /th> <
        th > Genre < /th> <
        th > Publisher < /th> <
        th > Number of Pages < /th> <
        th > Language < /th> <
        th > Rating < /th> <
        /tr> <
        /thead> <
        tbody > {
            filteredData.map((data, index) => ( <
                tr key = { index } >
                <
                td > { data.book_title } < /td> <
                td > { data.author } < /td> <
                td > { data.publication_date } < /td> <
                td > { data.genre } < /td> <
                td > { data.publisher } < /td> <
                td > { data.num_pages } < /td> <
                td > { data.language } < /td> <
                td > { data.rating } < /td> <
                /tr>
            ))
        } <
        /tbody> <
        /table> <
        /div>
    );
};

export default LibraryView;