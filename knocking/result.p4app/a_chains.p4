state parse_genhdr_uid1{
	pkt.extract(hdr.genhdr_uid1);
	transition accept;
}
state check_uid12{
	transition parse_genhdr_uid1;
}
#define CHAIN_IPV4_TCP
state chain_ipv4_tcp{
	transition check_uid12;
}
