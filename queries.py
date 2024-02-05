
#query to search races
#take out the single backslash before name after filters
search_query = """query fetchAllRaces($name: String!) {
  response {
    success
    errors
    result {
      races (filters: {name: $name}) {
        race {
          race_id
          name
          last_date
          last_end_date
          next_date
          next_end_date
          is_draft_race
          is_private_race
          is_registration_open
          created
          last_modified
          description
          url
          external_race_url
          external_results_url
          fb_page_id
          fb_event_id
          address {
            street
            street2
            city
            state
            zipcode
            country_code
          }
          timezone
          logo_url
          real_time_notifications_enabled
        }
      }
    }
  }
}"""

advanced_search_query = """query fetchAllRaces($name: String!, $city: String!, $state: String!, $country_code: String!) {
  advancedResponse {
    success
    errors
    result {
      races(
        filters: {name: $name, city: $city, state: $state, country_code: $country_code}
      ) {
        race {
          race_id
          name
          last_date
          last_end_date
          next_date
          next_end_date
          is_draft_race
          is_private_race
          is_registration_open
          created
          last_modified
          description
          url
          external_race_url
          external_results_url
          fb_page_id
          fb_event_id
          address {
            street
            street2
            city
            state
            zipcode
            country_code
          }
          timezone
          logo_url
          real_time_notifications_enabled
        }
      }
    }
  }
}"""

single_race_query = """query fetchRace($race_id: long!) {
  race_response {
    success
    errors
    result {
      race(filters: {race_id: $race_id}) {
        race_id
        name
        last_date
        last_end_date
        next_date
        next_end_date
        is_draft_race
        is_private_race
        is_registration_open
        created
        last_modified
        description
        url
        external_race_url
        external_results_url
        fb_page_id
        fb_event_id
        address {
          street
          street2
          city
          state
          zipcode
          country_code
        }
        timezone
        logo_url
        real_time_notifications_enabled
        events {
          event_id
          race_event_days_id
          name
          details
          start_time
          end_time
          age_calc_base_date
          registration_opens
          event_type
          distance
          volunteer
          require_dob
          require_phone
          registration_periods {
            registration_opens
            registration_closes
            race_fee
            processing_fee
          }
        }
        sub_event_ids
        giveaway
      }
    }
  }
}"""