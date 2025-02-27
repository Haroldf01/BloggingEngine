import React from 'react'
import { Header } from 'semantic-ui-react'

export default function BasicHeader() {
	let headers = <React.Fragment>
		<Header as='h1'>First Header</Header>
		<Header as='h2'>Second Header</Header>
		<Header as='h3'>Third Header</Header>
		<Header as='h4'>Fourth Header</Header>
		<Header as='h5'>Fifth Header</Header>
		<Header as='h6'>Sixth Header</Header>
	</React.Fragment>;

	return headers;
};
