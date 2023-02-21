ingress = bfrt.ntp_guard.pipe.SwitchIngress

ingress.exact_match_table_uid3.add_with_setter_action_uid4_true(0)
ingress.forward.add_with_send("00:11:22:33:44:55",0)
ingress.forward.add_with_send("00:aa:bb:cc:dd:ee",1)
ingress.forward.add_with_send("ff:ff:ff:ff:ff:ff",1)