if (hdr.genhdr_uid1.isValid()){
	ig_tm_md.ucast_egress_port = 8;
	exact_match_table_uid3.apply();
	if (exploit==1){
		ig_dprsr_md.drop_ctl = 0x1;
	}
}
