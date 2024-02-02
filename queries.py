
#query to search races
#take out the single backslash before name after filters
races_query = """query fetchAllRaces($name: String!) {
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