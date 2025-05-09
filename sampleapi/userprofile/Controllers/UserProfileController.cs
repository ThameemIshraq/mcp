using Microsoft.AspNetCore.Mvc;

namespace UserProfile.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class UserProfileController : ControllerBase
    {
         private static List<UserProfile> _userProfiles = new List<UserProfile>
        {
            new UserProfile { Id = 1, FirstName = "Alice", LastName = "Johnson", Email = "alice@example.com", DateOfBirth = new DateTime(1990, 5, 1) },
            new UserProfile { Id = 2, FirstName = "Bob", LastName = "Smith", Email = "bob@example.com", DateOfBirth = new DateTime(1985, 8, 20) }
        };
        public UserProfileController()
        {
           
        }

        [HttpGet]
       public ActionResult<IEnumerable<UserProfile>> GetAll()
        {
            return Ok(_userProfiles);
        }

        [HttpGet("{id}")]
        public ActionResult<UserProfile> GetById(int id)
        {
            var user = _userProfiles.FirstOrDefault(u => u.Id == id);
            if (user == null) return NotFound();
            return Ok(user);
        }

         [HttpPost]
        public ActionResult<UserProfile> Create(UserProfile profile)
        {
            profile.Id = _userProfiles.Max(u => u.Id) + 1;
            _userProfiles.Add(profile);
            return CreatedAtAction(nameof(GetById), new { id = profile.Id }, profile);
        }

       [HttpPut("{id}")]
        public IActionResult Update(int id, UserProfile updatedProfile)
        {
            var existing = _userProfiles.FirstOrDefault(u => u.Id == id);
            if (existing == null) return NotFound();

            existing.FirstName = updatedProfile.FirstName;
            existing.LastName = updatedProfile.LastName;
            existing.Email = updatedProfile.Email;
            existing.DateOfBirth = updatedProfile.DateOfBirth;

            return NoContent();
        }

       [HttpDelete("{id}")]
        public IActionResult Delete(int id)
        {
            var user = _userProfiles.FirstOrDefault(u => u.Id == id);
            if (user == null) return NotFound();

            _userProfiles.Remove(user);
            return NoContent();
        }
    }

     public class UserProfile
    {
        public int Id { get; set; }
        public string FirstName { get; set; } = string.Empty;
        public string LastName { get; set; } = string.Empty;
        public string Email { get; set; } = string.Empty;
        public DateTime DateOfBirth { get; set; }
    }
}


