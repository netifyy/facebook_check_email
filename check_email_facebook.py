
_='''
==============
[×] Name : Netify
[×] https://t.me/nev_bb
[×] country : America
==============
''';print(_)

import requests
import os
import random
import string
import sys
from random import choice 
class Facebook:
    def __init__(self):
        self.characters = string.ascii_letters + string.digits + "&=_:%-"
        self.random_string = ''.join(random.choice(self.characters) for _ in range(150))
        self.number = ''.join([str(random.randint(0, 9)) for _ in range(18)])
        self.number2 = int(self.number)
        self.new_number = self.generate_new_number()

    def generate_new_number(self):
        return ''.join(random.choice(string.digits) for _ in range(5))

    def send_request(self):
        email = input(" Email : ")  
        try:
            headers = {
                "Accept": "*/*",
                "Accept-Language": "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7",
                "Content-Length": "9704",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Cookie": "your_cookie_here",
                "Origin": "https://m.facebook.com",
                "Referer": "https://m.facebook.com/reg/",
                "Sec-Ch-Prefers-Color-Scheme": "dark",
                "Sec-Ch-Ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",                
                "Sec-Ch-Ua-Mobile": "?1",
                "Sec-Ch-Ua-Model": "\"Infinix X6816\"",
                "Sec-Ch-Ua-Platform": "\"Android\"",
                "Sec-Ch-Ua-Platform-Version": "\"11.0.0\"",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
                "Cookie": "datr=x1bHZqFIlum3zoy7mw7uSZmp; ps_l=1; ps_n=1; sb=DFfHZl1So6p69QUgUkHEZCJg; m_pixel_ratio=1.84375; x-referer=eyJyIjoiL2NoZWNrcG9pbnQvMTUwMTA5MjgyMzUyNTI4Mi9sb2dvdXQvP25leHQ9aHR0cHMlM0ElMkYlMkZtLmZhY2Vib29rLmNvbSUyRmxvZ2luJTJGc2F2ZS1kZXZpY2UlMkYlM0Zsb2dpbl9zb3VyY2UlM0RhY2NvdW50X2NyZWF0aW9uJTI2bG9nZ2VyX2lkJTNEYWU4MjZlNGMtMTEwOS00M2Q1LWE5ZGMtZThiNjg3ZWI5YzFhJnBhaXB2PTAmZWF2PUFmYTNMRmI0WDc3aUY1RGxHZU5VZzI1OXR2ZHVLRWdGUFVfeUVBYlpYZUVEaFVtN25VZTJVZVRzcjMyVEQ5eDVfUTAiLCJoIjoiL2NoZWNrcG9pbnQvMTUwMTA5MjgyMzUyNTI4Mi9sb2dvdXQvP25leHQ9aHR0cHMlM0ElMkYlMkZtLmZhY2Vib29rLmNvbSUyRmxvZ2luJTJGc2F2ZS1kZXZpY2UlMkYlM0Zsb2dpbl9zb3VyY2UlM0RhY2NvdW50X2NyZWF0aW9uJTI2bG9nZ2VyX2lkJTNEYWU4MjZlNGMtMTEwOS00M2Q1LWE5ZGMtZThiNjg3ZWI5YzFhJnBhaXB2PTAmZWF2PUFmYTNMRmI0WDc3aUY1RGxHZU5VZzI1OXR2ZHVLRWdGUFVfeUVBYlpYZUVEaFVtN25VZTJVZVRzcjMyVEQ5eDVfUTAiLCJzIjoibSJ9; wd=391x795; rs=22%7C08%7C2005%7C%7Cmaznsjad161%40gmail.com%7CDb%7CSam%7CDb+Sam; fr=0FM8cKuyJsx7ronHk.AWWKA39dq1nNR6nUeusWdVsJZTU.Bmx1bH..AAA.0.0.Bmx2AT.AWU9TRCWUPs"
            }
            data=f"__aaid=0&__user=0&__a=1&__req=w&__hs=19957.BP%3Awbloks_caa_pkg.2.0..0.0&dpr=1&__ccg=GOOD&__rev={self.new_number}&__s=%3A6p3c5f%3Ayqxzmf&__hsi={self.new_number}&__dyn={self.random_string}&jazoest=24903&lsd=AVpVO5qxedI&params=%7B%22params%22%3A%22%7B%5C%22server_params%5C%22%3A%7B%5C%22event_request_id%5C%22%3A%5C%2214287536-94c6-42b9-b16d-0a48010fb66b%5C%22%2C%5C%22cp_funnel%5C%22%3A0%2C%5C%22cp_source%5C%22%3A0%2C%5C%22text_input_id%5C%22%3A%5C%22145325470400060%5C%22%2C%5C%22reg_info%5C%22%3A%5C%22%7B%5C%5C%5C%22first_name%5C%5C%5C%22%3A%5C%5C%5C%22Oi%5C%5C%5C%22%2C%5C%5C%5C%22last_name%5C%5C%5C%22%3A%5C%5C%5C%22Ij%5C%5C%5C%22%2C%5C%5C%5C%22full_name%5C%5C%5C%22%3A%5C%5C%5C%22Oi+Ij%5C%5C%5C%22%2C%5C%5C%5C%22contactpoint%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ar_contactpoint%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22contactpoint_type%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_using_unified_cp%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22unified_cp_screen_variant%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_cp_auto_confirmed%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22is_cp_auto_confirmable%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22confirmation_code%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22birthday%5C%5C%5C%22%3A%5C%5C%5C%2222-08-2005%5C%5C%5C%22%2C%5C%5C%5C%22did_use_age%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22gender%5C%5C%5C%22%3A2%2C%5C%5C%5C%22use_custom_gender%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22custom_gender%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22encrypted_password%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22username%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22username_prefill%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22fb_conf_source%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22device_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig4a_qe_device_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22family_device_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22nta_eligibility_reason%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig_nta_test_group%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22user_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22safetynet_token%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22safetynet_response%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22machine_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22profile_photo%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22profile_photo_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22profile_photo_upload_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22avatar%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22email_oauth_token_no_contact_perm%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22email_oauth_token%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22email_oauth_tokens%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22should_skip_two_step_conf%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22openid_tokens_for_testing%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22encrypted_msisdn%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22encrypted_msisdn_for_safetynet%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22cached_headers_safetynet_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22should_skip_headers_safetynet%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22headers_last_infra_flow_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22headers_last_infra_flow_id_safetynet%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22headers_flow_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22was_headers_prefill_available%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22sso_enabled%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22existing_accounts%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22used_ig_birthday%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22sync_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22create_new_to_app_account%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22skip_session_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ck_error%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ck_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ck_nonce%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22should_save_password%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22horizon_synced_username%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22fb_access_token%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22horizon_synced_profile_pic%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_identity_synced%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22is_msplit_reg%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22user_id_of_msplit_creator%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22dma_data_combination_consent_given%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22xapp_accounts%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22fb_device_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22fb_machine_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig_device_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig_machine_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22should_skip_nta_upsell%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22big_blue_token%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22skip_sync_step_nta%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22caa_reg_flow_source%5C%5C%5C%22%3A%5C%5C%5C%22aymh_multi_profiles_native_integration_point%5C%5C%5C%22%2C%5C%5C%5C%22ig_authorization_token%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22full_sheet_flow%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22crypted_user_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_caa_perf_enabled%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22is_preform%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22ignore_suma_check%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22ignore_existing_login%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22ignore_existing_login_from_suma%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22ignore_existing_login_after_errors%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22suggested_first_name%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22suggested_last_name%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22suggested_full_name%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22replace_id_sync_variant%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22frl_authorization_token%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22post_form_errors%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22skip_step_without_errors%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22existing_account_exact_match_checked%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22existing_account_fuzzy_match_checked%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22confirmation_code_send_error%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_too_young%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22source_account_type%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22whatsapp_installed_on_client%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22confirmation_medium%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22source_credentials_type%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22source_cuid%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22source_account_reg_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22soap_creation_source%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22source_account_type_to_reg_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22registration_flow_id%5C%5C%5C%22%3A%5C%5C%5C%222e33f602-cefb-4d4e-a34b-223ba023c007%5C%5C%5C%22%2C%5C%5C%5C%22should_skip_youth_tos%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22is_youth_regulation_flow_complete%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22is_on_cold_start%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22email_prefilled%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22cp_confirmed_by_auto_conf%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22auto_conf_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22in_sowa_experiment%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22youth_regulation_config%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22conf_allow_back_nav_after_change_cp%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22conf_bouncing_cliff_screen_type%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22conf_show_bouncing_cliff%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22eligible_to_flash_call_in_ig4a%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22flash_call_permissions_status%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22attestation_result%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22request_data_and_challenge_nonce_string%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22confirmed_cp_and_code%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22in_updated_eu_tos%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22notification_callback_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22reg_suma_state%5C%5C%5C%22%3A0%2C%5C%5C%5C%22is_msplit_neutral_choice%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22zero_tap_enabled%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22msg_previous_cp%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ntp_import_source_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22youth_consent_decision_time%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22username_screen_experience%5C%5C%5C%22%3A%5C%5C%5C%22control%5C%5C%5C%22%2C%5C%5C%5C%22reduced_tos_test_group%5C%5C%5C%22%3A%5C%5C%5C%22control%5C%5C%5C%22%2C%5C%5C%5C%22should_show_spi_before_conf%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22google_oauth_account%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_reg_request_from_ig_suma%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22is_igios_spc_reg%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22device_emails%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_toa_reg%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22is_threads_public%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22spc_import_flow%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22caa_play_integrity_attestation_result%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22flash_call_provider%5C%5C%5C%22%3Anull%7D%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22flow_name%5C%5C%5C%22%3A%5C%5C%5C%22new_to_family_fb_default%5C%5C%5C%22%2C%5C%5C%5C%22flow_type%5C%5C%5C%22%3A%5C%5C%5C%22ntf%5C%5C%5C%22%7D%5C%22%2C%5C%22current_step%5C%22%3A4%2C%5C%22INTERNAL__latency_qpl_marker_id%5C%22%3A36707139%2C%5C%22INTERNAL__latency_qpl_instance_id%5C%22%3A%5C%22145325470400102%5C%22%2C%5C%22device_id%5C%22%3Anull%2C%5C%22family_device_id%5C%22%3Anull%2C%5C%22waterfall_id%5C%22%3A%5C%2244ad31ec-a41a-4825-a20b-74283e0e152e%5C%22%2C%5C%22offline_experiment_group%5C%22%3Anull%2C%5C%22layered_homepage_experiment_group%5C%22%3Anull%2C%5C%22is_platform_login%5C%22%3A0%2C%5C%22is_from_logged_in_switcher%5C%22%3A0%2C%5C%22is_from_logged_out%5C%22%3A0%2C%5C%22access_flow_version%5C%22%3A%5C%22F2_FLOW%5C%22%2C%5C%22INTERNAL_INFRA_THEME%5C%22%3A%5C%22harm_f%5C%22%7D%2C%5C%22client_input_params%5C%22%3A%7B%5C%22device_id%5C%22%3A%5C%22%5C%22%2C%5C%22family_device_id%5C%22%3A%5C%22%5C%22%2C%5C%22email%5C%22%3A%5C%22{email}%40gmail.com%5C%22%2C%5C%22email_prefilled%5C%22%3A0%2C%5C%22accounts_list%5C%22%3A%5B%5D%2C%5C%22fb_ig_device_id%5C%22%3A%5B%5D%2C%5C%22confirmed_cp_and_code%5C%22%3A%7B%7D%2C%5C%22is_from_device_emails%5C%22%3A0%2C%5C%22msg_previous_cp%5C%22%3A%5C%22%5C%22%2C%5C%22lois_settings%5C%22%3A%7B%5C%22lois_token%5C%22%3A%5C%22%5C%22%2C%5C%22lara_override%5C%22%3A%5C%22%5C%22%7D%7D%7D%22%7D"
            
            response = requests.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.async.contactpoint_email.async&type=action&__bkv=c57d4920c3c36f22d3b4e5020400255a25a3c0c888490a172b92d1942fc03cf6", headers=headers, data=data).text   
            if "CAA_REG_EMAIL_LOGIN_UPSELL" in response:               
                print("Done Email")                                                    
            elif "CAA_REG_MSPLIT" in response:
            	print("Bad Email")
            elif "USER_REGISTER_EMAIL_DISABLED" in response:
            	print('bad Email2')            
            else:
            	print(response)
            

        except Exception as e:
            print(f" {e}")

if __name__ == "__main__":
    while True:
    	fb = Facebook()
    	fb.send_request()